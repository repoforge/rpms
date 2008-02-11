# $Id$
# Authority: dag

Summary: Video DVD backup tool
Name: k9copy
Version: 1.1.0
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://k9copy.sf.net/

Source: http://dl.sf.net/k9copy/k9copy-%{version}.tar.gz
Source1: http://dl.sf.net/vamps/vamps-0.99.2.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++

%description
k9copy is a DVD backup utility which allows copying of one or more titles
from a 9.6 GB DVD to a normal DVD.

%prep
%setup -a 1

%build
source /etc/profile.d/qt.sh
%configure
%{__make} -C vamps-* %{?_smp_mflags} PREFIX="%{_prefix}" CFLAGS="%{optflags} -DHAVE_BUILTIN_EXPECT"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%{__make} install -C vamps-* PREFIX="%{buildroot}%{_prefix}"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_docdir}/HTML/*/k9copy/
%{_bindir}/*
%{_libdir}/libk9copy.so*
%{_datadir}/applnk/Multimedia/k9copy.desktop
%{_datadir}/apps/konqueror/servicemenus/k9copy_open.desktop
%{_datadir}/apps/k9copy
%{_datadir}/icons/*/*/*/*
%exclude %{_includedir}

%changelog
* Sun Mar 11 2007 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Initial package. (using DAR)
