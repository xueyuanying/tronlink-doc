# Android 12 SplashScreen 迁移方案

## 目录
- [背景介绍](#背景介绍)
- [当前实现分析](#当前实现分析)
- [Android 12 SplashScreen 新特性](#android-12-splashscreen-新特性)
- [迁移方案](#迁移方案)
- [实施计划](#实施计划)
- [注意事项](#注意事项)
- [风险评估](#风险评估)
- [后续优化](#后续优化)

## 背景介绍

Android 12 引入了新的 SplashScreen API，这是一个系统级的启动页实现，旨在提供更统一、更流畅的应用启动体验。从 Android 12 开始，系统会强制使用新的 SplashScreen API，因此我们需要对现有的启动页实现进行迁移。

## 当前实现分析

### 现有实现
1. 使用 `WelcomeActivity` 作为启动页 Activity
2. 主题配置：
```xml
<style name="welcome" parent="Theme.AppCompat.NoActionBar">
    <item name="android:windowNoTitle">true</item>
    <item name="android:windowFullscreen">true</item>
    <item name="android:windowBackground">@color/white</item>
    <item name="android:windowTranslucentStatus">true</item>
    <item name="android:windowTranslucentNavigation">true</item>
    <item name="android:windowDisablePreview">true</item>
    <item name="android:fontFamily">@font/lato</item>
</style>
```

3. 启动页内容：
- 支持显示 GIF 动画
- 支持显示静态图片
- 支持从服务器下载启动页图片
- 包含进度条显示功能

### 存在的问题
1. 在 Android 12 及以上版本，系统会强制使用新的 SplashScreen API
2. 当前实现可能导致启动时出现白屏闪烁
3. 启动页切换动画不够流畅
4. 没有适配深色模式
5. 启动页资源加载可能影响启动速度

## Android 12 SplashScreen 新特性

### 核心特性
1. 系统级启动页，由系统统一管理
2. 支持自定义启动页图标、背景色
3. 支持启动页退出动画
4. 支持深色模式
5. 支持动态调整启动页样式
6. 支持自定义启动页持续时间

### 优势
1. 更快的启动速度
2. 更流畅的过渡动画
3. 更好的系统集成
4. 更统一的用户体验
5. 更好的内存管理
6. 更简单的实现方式

## 迁移方案

### 1. 基础适配

#### 1.1 添加依赖
```gradle
dependencies {
    implementation "androidx.core:core-splashscreen:1.0.1"
}
```

#### 1.2 创建启动页主题
```xml
<!-- res/values/themes.xml -->
<style name="Theme.App.Starting" parent="Theme.SplashScreen">
    <item name="windowSplashScreenBackground">@color/white</item>
    <item name="windowSplashScreenAnimatedIcon">@drawable/ic_launcher_foreground</item>
    <item name="windowSplashScreenAnimationDuration">300</item>
    <item name="postSplashScreenTheme">@style/Theme.AppCompat.NoActionBar</item>
</style>

<!-- res/values-night/themes.xml -->
<style name="Theme.App.Starting" parent="Theme.SplashScreen">
    <item name="windowSplashScreenBackground">@color/black</item>
    <item name="windowSplashScreenAnimatedIcon">@drawable/ic_launcher_foreground</item>
    <item name="windowSplashScreenAnimationDuration">300</item>
    <item name="postSplashScreenTheme">@style/Theme.AppCompat.NoActionBar</item>
</style>
```

#### 1.3 修改 AndroidManifest.xml
```xml
<activity
    android:name=".business.welcome.WelcomeActivity"
    android:theme="@style/Theme.App.Starting"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

### 2. 功能适配

#### 2.1 保留现有功能
- 服务器图片下载
- GIF 动画支持
- 进度条显示
- 多语言支持

#### 2.2 新增功能
- 启动页退出动画
- 深色模式支持
- 动态主题切换
- 启动页状态监听

### 3. 代码适配

#### 3.1 WelcomeActivity 改造
```java
public class WelcomeActivity extends BaseActivity {
    private SplashScreen splashScreen;
    private AcWelcomeBinding binding;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // 在 super.onCreate 之前安装 SplashScreen
        splashScreen = SplashScreen.installSplashScreen(this);
        
        super.onCreate(savedInstanceState);
        
        // 设置启动页退出监听
        splashScreen.setOnExitAnimationListener(splashScreenProvider -> {
            // 创建自定义退出动画
            final Object splashScreenView = splashScreenProvider.getView();
            final Object splashScreenIconView = splashScreenProvider.getIconView();
            
            // 创建动画
            Object exitAnimation = createExitAnimation();
            
            // 执行动画
            exitAnimation.addListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animation) {
                    splashScreenProvider.remove();
                }
            });
            exitAnimation.start();
        });
        
        // 初始化视图
        initializeViews();
        
        // 加载启动页资源
        loadSplashResources();
    }
    
    private void loadSplashResources() {
        // 检查是否需要从服务器下载启动页图片
        if (needDownloadSplashImage()) {
            downloadSplashImage();
        } else {
            showDefaultSplash();
        }
    }
    
    private void showDefaultSplash() {
        // 显示默认启动页
        binding.simpleDraweeView.setGif(R.drawable.welcome, 1, 100, null);
        binding.simpleDraweeView.setVisibility(View.VISIBLE);
        binding.sloganTextView.setVisibility(View.VISIBLE);
    }
}
```

#### 3.2 动画实现
```java
private Object createExitAnimation() {
    // 创建启动页退出动画
    ObjectSet<Animator> animators = new ObjectSet<>();
    
    // 图标动画
    Object iconAnimator = ObjectAnimator.ofFloat(
        splashScreenIconView,
        "alpha",
        1f,
        0f
    );
    iconAnimator.setDuration(300);
    animators.add(iconAnimator);
    
    // 背景动画
    Object backgroundAnimator = ObjectAnimator.ofFloat(
        splashScreenView,
        "alpha",
        1f,
        0f
    );
    backgroundAnimator.setDuration(300);
    animators.add(backgroundAnimator);
    
    // 创建动画集合
    Object animatorSet = new AnimatorSet();
    animatorSet.playTogether(animators);
    
    return animatorSet;
}
```

### 4. 官方推荐的最佳实践

#### 4.1 保留自定义启动页 Activity
如果出于品牌推广原因需要保留自定义启动页 Activity，可以通过以下方式实现：
```java
public class RoutingActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SplashScreen splashScreen = SplashScreen.installSplashScreen(this);
        super.onCreate(savedInstanceState);
        
        // 保持启动画面可见
        splashScreen.setKeepOnScreenCondition(() -> true);
        startSomeNextActivity();
        finish();
    }
}
```

#### 4.2 移除自定义启动页 Activity
建议移除自定义启动页 Activity，以提高效率并缩短启动时间：

1. 使用延迟加载
   - 避免在启动时加载不必要的组件
   - 使用 App Startup 库进行组件初始化
   - 确保 Application.onCreate() 轻量化

2. 使用占位符
   - 在本地加载少量数据时创建占位符
   - 对于网络加载，显示异步加载的占位符
   - 在内容区域应用巧妙的动画效果

3. 使用缓存
   - 首次打开时显示加载指示
   - 后续打开时使用缓存内容
   - 后台更新最新内容

## 实施计划

### 第一阶段：基础适配（预计 2 天）
1. 添加 SplashScreen 依赖
2. 创建新的启动页主题
3. 配置 AndroidManifest.xml
4. 实现基础启动页功能

### 第二阶段：功能增强（预计 3 天）
1. 实现启动页退出动画
2. 添加深色模式支持
3. 优化过渡效果
4. 实现动态主题切换

### 第三阶段：测试优化（预计 2 天）
1. 兼容性测试
   - 测试不同 Android 版本
   - 测试不同机型
   - 测试不同分辨率
2. 性能测试
   - 启动速度测试
   - 内存使用测试
   - 动画流畅度测试
3. 用户体验优化
   - 收集用户反馈
   - 优化动画效果
   - 完善错误处理

## 注意事项

### 1. 兼容性处理
- 需要保持对 Android 12 以下版本的兼容
- 使用版本判断进行适配
- 提供降级方案

### 2. 性能优化
- 控制启动页资源大小
- 优化资源加载时机
- 避免不必要的网络请求
- 使用延迟加载和缓存机制

### 3. 用户体验
- 确保动画流畅
- 保持品牌一致性
- 提供良好的错误提示
- 优化启动时间

### 4. 代码质量
- 遵循代码规范
- 添加必要的注释
- 做好异常处理
- 使用官方推荐的最佳实践

## 风险评估

### 1. 兼容性风险
- 部分老旧机型可能存在兼容性问题
- 不同 Android 版本表现不一致
- 解决方案：提供降级方案，做好版本判断

### 2. 性能风险
- 启动页加载可能影响启动速度
- 动画可能造成卡顿
- 解决方案：优化资源加载，控制动画复杂度

### 3. 用户体验风险
- 动画效果可能不够流畅
- 启动页切换可能不够自然
- 解决方案：充分测试，收集用户反馈

## 后续优化

### 1. 功能优化
- 支持更多自定义选项
- 添加更多动画效果
- 优化启动速度
- 完善深色模式支持

### 2. 体验优化
- 完善深色模式
- 添加更多主题支持
- 优化过渡效果
- 提升启动体验

### 3. 性能优化
- 优化资源加载
- 减少内存占用
- 提升启动速度
- 实现更高效的缓存机制

### 4. 维护优化
- 完善文档
- 添加单元测试
- 优化代码结构
- 遵循官方最佳实践 