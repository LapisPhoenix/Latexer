from dataclasses import dataclass


class LaTeXConstructor:

    class MathConstructs:
        @staticmethod
        def fraction(numerator: str | int | float, denominator: str | int | float) -> str:
            """
            Create a LaTeX fraction with a given numerator and denominator.

            :param numerator: The number (or equation) on top of the fraction.
            :param denominator: The number (or equation) on the bottom of the fraction.
            :return: LaTeX fraction string
            """
            return f"\\frac{{{numerator}}}{{{denominator}}}"

        @staticmethod
        def f_prime() -> str:
            """
            :return: LaTeX representation of f prime (f')
            """
            return "f’"

        @staticmethod
        def sqrt(number: str | int | float) -> str:
            """
            Create a LaTeX Square Root.

            :param number: The number (or equation) inside the square root.
            :return: LaTeX square root string
            """
            return f"\\sqrt{{{number}}}"

        @staticmethod
        def power_sqrt(power: str | int | float, number: str | int | float) -> str:
            """
            Create a LaTeX Square Root raised to the power of n.

            :param power: The power to which the square root is raised.
            :param number: The number inside the square root.
            :return: LaTeX power square root string
            """
            return f"\\sqrt[{power}]{{{number}}}"

        @staticmethod
        def overline(number: str | int | float) -> str:
            """
            Create a LaTeX overline.
            :param number: Number (or equation) UNDER the overline.
            :return: LaTeX overline
            """
            return f"\\overline{{{number}}}"

        @staticmethod
        def underline(number: str | int | float) -> str:
            """
            Create a LaTeX underline.
            :param number: Number (or equation) OVER the underline.
            :return: LaTeX underline
            """
            return f"\\underline{{{number}}}"

        @staticmethod
        def widehat(number: str | int | float) -> str:
            """
            Create a LaTeX widehat
            :param number: Number for widehat
            :return: LaTeX widehat
            """
            return f"\\widehat{{{number}}}"

        @staticmethod
        def widetilde(number: str | int | float) -> str:
            """
            Create a LaTeX widetilde
            :param number: Number for widetilde
            :return: LaTeX widetilde
            """
            return f"\\widetilde{{{number}}}"

        @staticmethod
        def overrightarrow(number: str | int | float) -> str:
            """
            Create a LaTex over right arrow
            :param number: Number for over right arrow
            :return: LaTeX overrightarrow
            """
            return f"\\overrightarrow{{{number}}}"
        @staticmethod
        def overleftarrow(number: str | float | int) -> str:
            """
            Create a LaTeX overleftarrow.
            :param number: Number (or equation) UNDER the overleftarrow.
            :return: LaTeX overleftarrow
            """
            return f"\\overleftarrow{{{number}}}"

        @staticmethod
        def overbrace(number: str | float | int) -> str:
            """
            Create a LaTeX overbrace.
            :param number: Number (or equation) UNDER the overbrace.
            :return: LaTeX overbrace
            """
            return f"\\overbrace{{{number}}}"

        @staticmethod
        def underbrace(number: str | float | int) -> str:
            """
            Create a LaTeX underbrace.
            :param number: Number (or equation) OVER the underbrace.
            :return: LaTeX underbrace
            """
            return f"\\underbrace{{{number}}}"

    @dataclass
    class Delimiter:
        PIPE: str = "|"
        VERT: str = "\\vert"
        LEFT_BRACE: str = "\\{"
        RIGHT_BRACE: str = "\\}"
        RIGHT_ANGLE: str = "\\rangle"
        LEFT_ANGLE: str = "\\langle"
        LEFT_FLOOR: str = "\\lfloor"
        RIGHT_FLOOR: str = "\\rfloor"
        LEFT_CEIL: str = "\\lceil"
        RIGHT_CEIL: str = "\\rceil"
        FORWARD_SLASH: str = "/"
        BACKSLASH: str = "\\"
        LEFT_BRACKET: str = "["
        RIGHT_BRACKET: str = "]"
        DOUBLE_UP_ARROW: str = "\\Uparrow"
        UP_ARROW: str = "\\uparrow"
        DOUBLE_DOWN_ARROW: str = "\\Downarrow"
        DOWN_ARROW: str = "\\downarrow"
        LEFT_LOWER_CORNER = "\\llcorner"
        RIGHT_LOWER_CORNER = "\\lrcorner"
        UPPER_LEFT_CORNER = "\\ulcorner"
        UPPER_RIGHT_CORNER = "\\urcorner"

    @dataclass
    class MathSymbols:
        ALPHA = "\\alpha"
        BETA = "\\beta"
        CHI = "\\chi"
        DELTA = "\\delta"
        EPSILON = "\\epsilon"
        ETA = "\\eta"
        GAMMA = "\\gamma"
        IOTA = "\\iota"
        KAPPA = "\\kappa"
        LAMBDA = "\\lambda"
        MU = "\\mu"
        NU = "\\nu"
        O = "o"             # noqa
        OMEGA = "\\omega"
        PHI = "\\phi"
        PI = "\\pi"
        PSI = "\\psi"
        RHO = "\\rho"
        SIGMA = "\\sigma"
        TAU = "\\tau"
        THETA = "\\theta"
        UPSILON = "\\upsilon"
        XI = "\\xi"
        ZETA = "\\zeta"
        DIGAMMA = "\\digamma"
        VAREPSILON = "\\varepsilon"
        VARKAPPA = "\\varkappa"
        VARPHI = "\\varphi"
        VARPI = "\\varpi"
        VARRHO = "\\varrho"
        VARSIGMA = "\\varsigma"
        VARTHETA = "\\vartheta"
        DELTA_UPPER = "\\Delta"
        GAMMA_UPPER = "\\Gamma"
        LAMBDA_UPPER = "\\Lambda"
        OMEGA_UPPER = "\\Omega"
        PHI_UPPER = "\\Phi"
        PI_UPPER = "\\Pi"
        PSI_UPPER = "\\Psi"
        SIGMA_UPPER = "\\Sigma"
        THETA_UPPER = "\\Theta"
        UPSILON_UPPER = "\\Upsilon"
        XI_UPPER = "\\Xi"
        ALEPH = "\\aleph"
        BETH = "\\beth"
        DALETH = "\\daleth"
        GIMEL = "\\gimel"

    @dataclass
    class Symbols:
        SUM = "\\sum"
        PROD = "\\prod"
        CO_PROD = "\\coprod"
        INT = "\\int"
        OINT = "\\oint"
        IINT = "\\iint"
        BIG_U_PLUS = "\\biguplus"
        BIG_CAP = "\\bigcap"
        BIG_CUP = "\\bigcup"
        BIG_O_PLUS = "\\bigoplus"
        BIG_O_TIMES = "\\bigotimes"
        BIG_O_DOT = "\\bigodot"
        BIG_VEE = "\\bigvee"
        BIG_WEDGE = "\\bigwedge"
        BIG_SQUARE_CUP = "\\bigsqcup"
