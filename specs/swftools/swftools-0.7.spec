# $Id$
# Authority: dag

Summary: Tools for SWF (Flash) animations under linux
Name: swftools
Version: 0.7.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.swftools.org/

Source: http://www.swftools.org/swftools-%{version}.tar.gz
Patch0: swftools-0.7.0-destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, flex, zlib-devel, libjpeg-devel, t1lib-devel
#BuildRequires: libavifile-devel
Conflicts: ming

%description
SWF Tools is a collection of SWF manipulation and generation utilities.

%prep
%setup
%patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING TODO
%doc %{_mandir}/man1/*.1*
%{_bindir}/*
%_datadir/swftools/

%changelog
* Mon Jan 22 2007 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Initial package. (using DAR)
