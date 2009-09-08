Summary:	Vifm is a ncurses based file manager with vi like keybindings
Summary(hu.UTF-8):	Vifm egy ncurses-alapú fájlkezelő vi-szerű billentyűzetkombinációkkal.
Summary(pl.UTF-8):	Menedżer plików oparty o ncurses obsługiwany komendami zaczerpniętymi z vi.
Name:		vifm
Version:	0.5
Release:	1
License:	GPL v2
Patch0:		%{name}-fix-datadir.patch
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/vifm/%{name}-%{version}.tar.bz2
# Source0-md5:	76818f02d6acd4997d1f41db932438aa
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
%patch0 -p1

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
install src/vifmrc $RPM_BUILD_ROOT%{_datadir}/vifm/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pauseme
%attr(755,root,root) %{_bindir}/vifm
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/vifm-help.txt
%{_datadir}/%{name}/vifm.txt
%{_datadir}/%{name}/vifm.vim
%{_datadir}/%{name}/vifmrc
