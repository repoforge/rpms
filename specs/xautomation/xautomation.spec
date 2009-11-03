# $Id$
# Authority: dries
# Upstream: Steve Slaven <junk_freshmeat$hoopajoo,net>


%{?el4:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Control input to X Windows from the command line
Name: xautomation
Version: 1.01
Release: 1%{?dist}
License: GPL
Group:  User Interface/X
URL: http://www.hoopajoo.net/projects/xautomation.html

Source: http://www.hoopajoo.net/static/projects/xautomation-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_modxorg:BuildRequires: libXtst-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Control X from the command line for scripts, and do "visual scraping" to
find things on the screen. The conrol interface allows mouse movement,
clicking, button up/down, key up/down, etc, and uses the XTest extension so
you don't have the annoying problems that xse has when apps ignore sent
events. The visgrep program find images inside of images and reports the
coordinates, allowing programs to find buttons etc. on the screen to click on.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/pat2ppm.1*
%doc %{_mandir}/man1/patextract.1*
%doc %{_mandir}/man1/png2pat.1*
%doc %{_mandir}/man1/rgb2pat.1*
%doc %{_mandir}/man1/visgrep.1*
%doc %{_mandir}/man1/xmousepos.1*
%doc %{_mandir}/man1/xte.1*
%doc %{_mandir}/man7/xautomation.7*
%{_bindir}/pat2ppm
%{_bindir}/patextract
%{_bindir}/png2pat
%{_bindir}/rgb2pat
%{_bindir}/visgrep
%{_bindir}/xmousepos
%{_bindir}/xte

%changelog
* Fri Jan 25 2008 Juan Carlos Castro y Castro <jcastro@instant.com.br> - 1.01-1
- Initial package.
