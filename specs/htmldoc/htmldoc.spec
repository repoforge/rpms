# $Id$

Summary: HTMLDOC html to pdf converter
Name: htmldoc
Version: 1.8.27
Release: 2%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.htmldoc.org/

Source: http://ftp.easysw.com/pub/htmldoc/%{version}/htmldoc-%{version}-source.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: automake, libtool

%description
htmldoc allows you to convert html pages to pdf format.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    bindir="%{buildroot}%{_bindir}" \
    datadir="%{buildroot}%{_datadir}" \
    mandir="%{buildroot}%{_mandir}"
%{__mv} %{buildroot}%{_datadir}/doc/htmldoc _rpmdocs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt _rpmdocs/*
%doc %{_mandir}/man1/htmldoc.1*
%{_bindir}/htmldoc
%{_datadir}/htmldoc/

%changelog
* Wed Oct 29 2008 Dag Wieers <dag@wieers.com> - 1.8.27-2
- Fixed Group.

* Thu Apr 17 2008 - Jim Nelson <jim.nelson@neteasyinc.com> - 1.8.27-1
- initial package
