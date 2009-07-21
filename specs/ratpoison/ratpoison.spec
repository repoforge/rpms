# $Id$
# Authority: dries
# Upstream: Shawn <sabetts$users,sourceforge,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Ratpoison window manager
Name: ratpoison
Version: 1.4.5
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://www.nongnu.org/ratpoison/

Source:  http://savannah.nongnu.org/download/ratpoison/ratpoison-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_modxorg:BuildRequires: libXtst-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Ratpoison is a simple Window Manager with no fat library dependencies, no
fancy graphics, no window decorations, and no flashy wank. It is largely
modelled after GNU Screen which has done wonders in virtual terminal market.
All interaction with the window manager is done through keystrokes.
ratpoison has a prefix map to minimize the key clobbering that cripples
EMACS and other quality pieces of software.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%postun
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_infodir}/ratpoison.info*
%doc %{_mandir}/man1/ratpoison.1*
%{_bindir}/ratpoison
%{_bindir}/rpws
%{_datadir}/ratpoison/
%exclude %{_datadir}/doc/ratpoison/

%changelog
* Fri Jul 17 2009 Dag Wieers <dag@wieers.com> - 1.4.5-1
- Updated to release 1.4.5.

* Sat Feb 23 2008 Dries Verachtert <dries@ulyssis.org> - 1.4.3-1
- Updated to release 1.4.3.

* Fri Jan 25 2008 Juan Carlos Castro y Castro <jcastro@instant.com.br> - 1.4.2-1
- Initial package.
