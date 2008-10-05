Summary:	Vifm is a ncurses based file manager with vi like keybindings
Summary(hu.UTF-8):	Vifm egy ncurses-alapú fájlkezelő vi-szerű billentyűzetkombinációkkal.
Name:		vifm
Version:	0.4
Release:	1
License:	GPL
Patch0:		%{name}-fix-datadir.patch
Patch1:		%{name}-use_malloc.patch
Group:		Applications/Shells
Source0:	http://dl.sourceforge.net/vifm/%{name}-%{version}.tar.bz2
# Source0-md5:	645071e1449d44d7957b78c1c094e454
URL:		http://vifm.sourceforge.net
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vifm is a ncurses based file manager with vi like keybindings.

%description -l hu.UTF-8
Vifm egy ncurses-alapú fájlkezelő vi-szerű billentyűzetkombinációkkal.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
