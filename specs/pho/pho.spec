# $Id$
# Authority: dag

Summary: Lightweight image viewer
Name: pho
Version: 0.9.5
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.shallowsky.com/software/pho/

Source: http://www.shallowsky.com/software/pho/pho-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: gtk+-devel >= 1.2
Buildrequires: gdk-pixbuf-devel >= 0.14

%description
Pho is a lightweight image browser.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 pho %{buildroot}%{_bindir}/pho
%{__install} -Dp -m0644 pho.1 %{buildroot}%{_mandir}/man1/pho.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README TODO *.html *.jpg
%doc %{_mandir}/man1/pho.1*
%{_bindir}/pho

%changelog
* Sun May 06 2007 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Initial package. (using DAR)
