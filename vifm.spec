Summary:	Vifm is a ncurses based file manager with vi like keybindings
Summary(hu.UTF-8):	Vifm egy ncurses-alapú fájlkezelő vi-szerű billentyűzetkombinációkkal.
Summary(pl.UTF-8):	Menedżer plików oparty o ncurses obsługiwany komendami zaczerpniętymi z vi.
Name:		vifm
Version:	0.7.1
Release:	1
License:	GPL v2
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/vifm/%{name}-%{version}.tar.bz2
# Source0-md5:	b90b05266a3a0159aa1ce88cb163a2fd
URL:		http://vifm.sourceforge.net/
BuildRequires:	ncurses-devel
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

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/vifm
%attr(755,root,root) %{_bindir}/vifm-pause
%attr(755,root,root) %{_bindir}/vifmrc-converter
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vifmrc
%{_datadir}/%{name}/vifm-help.txt*
%{_mandir}/man1/vifm.*
