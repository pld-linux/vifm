Summary:	Vifm is a ncurses based file manager with vi like keybindings
Summary(hu.UTF-8):	Vifm egy ncurses-alapú fájlkezelő vi-szerű billentyűzetkombinációkkal.
Summary(pl.UTF-8):	Menedżer plików oparty o ncurses obsługiwany komendami zaczerpniętymi z vi.
Name:		vifm
Version:	0.14.3
Release:	1
License:	GPL v2+
Group:		Applications/Shells
Source0:	https://downloads.sourceforge.net/vifm/%{name}-%{version}.tar.bz2
# Source0-md5:	11950e7e3f58b4f25d7cab000cdffb56
URL:		https://vifm.info/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	coreutils >= 7.6
BuildRequires:	glib2-devel
BuildRequires:	groff
BuildRequires:	libmagic-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	util-linux
BuildRequires:	xorg-lib-libX11-devel
Requires:	coreutils >= 7.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vifm is a ncurses based file manager with vi like keybindings.

%description -l hu.UTF-8
Vifm egy ncurses-alapú fájlkezelő vi-szerű billentyűzetkombinációkkal.

%description -l pl.UTF-8
Vifm jest menedżerem plików obsługiwanym za pomocą komend
analogicznych do komend programu vi. Interfejs vifm jest napisany w
ncurses.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' src/vifm-convert-dircolors

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	HAVE_FILE_PROG=1 \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.3party ChangeLog FAQ NEWS README TODO
%dir %{_sysconfdir}/vifm
%dir %{_sysconfdir}/vifm/colors
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vifm/colors/Default-256.vifm
%attr(755,root,root) %{_bindir}/vifm
%attr(755,root,root) %{_bindir}/vifm-convert-dircolors
%attr(755,root,root) %{_bindir}/vifm-pause
%attr(755,root,root) %{_bindir}/vifm-screen-split
%{_datadir}/%{name}
%{_mandir}/man1/vifm.*
%{_mandir}/man1/vifm-convert-dircolors.1*
%{_mandir}/man1/vifm-pause.1*
%{_mandir}/man1/vifm-screen-split.1*
%{_desktopdir}/vifm.desktop
%{_iconsdir}/hicolor/*x*/apps/vifm.png
%{_iconsdir}/hicolor/scalable/apps/vifm.svg
%{_pixmapsdir}/vifm.png
%{bash_compdir}/vifm
%{fish_compdir}/vifm.fish
%{zsh_compdir}/_vifm
