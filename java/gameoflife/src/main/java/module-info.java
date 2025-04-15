module com.github.innovationsquared {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.github.innovationsquared to javafx.fxml;
    exports com.github.innovationsquared;
}
