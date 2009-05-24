# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Light-weight system monitor for X
Name: conky
Version: 1.6.1
Release: 1
License: GPL
Group: Applications/System
URL: http://conky.sourceforge.net/

Source: http://dl.sf.net/conky/conky-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libXdamage-devel, libXfixes-devel, libXext-devel, glib2-devel}

%description
Conky is a free, light-weight system monitor for X, that displays any 
information on your desktop.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} prefix="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/conky.1*
%config(noreplace) %{_sysconfdir}/conky/conky.conf
%{_bindir}/conky
%dir %{_sysconfdir}/conky/

%changelog
* Sun Apr 19 2009 Dries Verachtert <dries@ulyssis.org> - 1.6.1-1
- Initial package.
