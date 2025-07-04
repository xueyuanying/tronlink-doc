# Android 12 SplashScreen 适配方案

## 一、背景分析

### 1.1 当前实现
- 使用自定义 Activity 作为启动页
- 通过 Handler 延迟跳转
- 使用 GIF 动画展示
- 包含权限检查等业务逻辑

### 1.2 存在的问题
- 启动页显示不够流畅
- 与系统启动页存在重复
- 不符合 Android 12 新规范
- 用户体验不够统一

## 二、适配方案

### 2.1 核心特性
1. 使用 AndroidX SplashScreen 库
2. 保留现有业务逻辑
3. 优化启动体验
4. 统一品牌展示

### 2.2 具体实现

#### 2.2.1 依赖配置
```gradle
dependencies {
    implementation 'androidx.core:core-splashscreen:1.0.1'
}
```

#### 2.2.2 主题配置
1. 日间模式主题：
```xml
<!-- app/src/main/res/values/themes.xml -->
<style name="Theme.App.Starting" parent="Theme.SplashScreen">
    <item name="windowSplashScreenBackground">@color/white</item>
    <item name="windowSplashScreenAnimatedIcon">@drawable/ic_launcher_foreground</item>
    <item name="windowSplashScreenAnimationDuration">1000</item>
    <item name="postSplashScreenTheme">@style/Theme.AppCompat.Light.NoActionBar</item>
</style>
```

2. 夜间模式主题：
```xml
<!-- app/src/main/res/values-night/themes.xml -->
<style name="Theme.App.Starting" parent="Theme.SplashScreen">
    <item name="windowSplashScreenBackground">@color/black</item>
    <item name="windowSplashScreenAnimatedIcon">@drawable/ic_launcher_foreground</item>
    <item name="windowSplashScreenAnimationDuration">1000</item>
    <item name="postSplashScreenTheme">@style/Theme.AppCompat.NoActionBar</item>
</style>
```

#### 2.2.3 启动页资源
1. 日间模式启动图标：
```xml
<!-- app/src/main/res/drawable/ic_launcher_foreground.xml -->
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <group
        android:scaleX="0.5"
        android:scaleY="0.5"
        android:translateX="27"
        android:translateY="27">
        <path
            android:fillColor="#FFFFFF"
            android:pathData="M54,54m-48,0a48,48 0,1 1,96 0a48,48 0,1 1,-96 0" />
        <path
            android:fillColor="#000000"
            android:pathData="M54,54m-40,0a40,40 0,1 1,80 0a40,40 0,1 1,-80 0" />
    </group>
</vector>
```

2. 夜间模式启动图标：
```xml
<!-- app/src/main/res/drawable-night/ic_launcher_foreground.xml -->
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <group
        android:scaleX="0.5"
        android:scaleY="0.5"
        android:translateX="27"
        android:translateY="27">
        <path
            android:fillColor="#000000"
            android:pathData="M54,54m-48,0a48,48 0,1 1,96 0a48,48 0,1 1,-96 0" />
        <path
            android:fillColor="#FFFFFF"
            android:pathData="M54,54m-40,0a40,40 0,1 1,80 0a40,40 0,1 1,-80 0" />
    </group>
</vector>
```

#### 2.2.4 代码实现
```java
public class WelcomeActivity extends BaseActivity {
    private SplashScreen splashScreen;
    private static final int SPLASH_DURATION = 1000;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // 在 super.onCreate 之前安装 SplashScreen
        splashScreen = SplashScreen.installSplashScreen(this);
        super.onCreate(savedInstanceState);
        
        // 设置退出动画
        splashScreen.setOnExitAnimationListener(splashScreenProvider -> {
            final ObjectAnimator fadeOut = ObjectAnimator.ofFloat(
                splashScreenProvider.getView(),
                View.ALPHA,
                1f,
                0f
            );
            fadeOut.setInterpolator(new DecelerateInterpolator());
            fadeOut.setDuration(SPLASH_DURATION);

            fadeOut.addListener(new AnimatorListenerAdapter() {
                @Override
                public void onAnimationEnd(Animator animation) {
                    splashScreenProvider.remove();
                }
            });

            fadeOut.start();
        });

        // 保留原有的业务逻辑
        setContentView(R.layout.activity_welcome);
        initView();
        initData();
    }
}
```

### 2.3 优化效果
1. 启动体验
   - 更快的启动速度
   - 更流畅的过渡动画
   - 统一的品牌展示

2. 代码质量
   - 符合 Android 12 规范
   - 保留原有业务逻辑
   - 代码结构清晰

3. 维护性
   - 使用官方推荐方案
   - 减少自定义代码
   - 便于后续升级

## 三、注意事项

### 3.1 兼容性处理
- 使用 AndroidX SplashScreen 库确保兼容性
- 保持原有业务逻辑不变
- 适配不同 Android 版本

### 3.2 性能优化
- 控制启动页资源大小
- 优化动画性能
- 减少不必要的初始化

### 3.3 测试验证
- 验证不同设备上的表现
- 确保业务逻辑正常
- 检查内存占用情况

## 四、后续优化

### 4.1 计划优化项
1. 优化启动页资源
2. 完善错误处理
3. 添加性能监控

### 4.2 长期规划
1. 持续跟进官方更新
2. 优化用户体验
3. 提升启动性能 