# $Id$

# Authority: dag

%define real_name XML-LibXML-Common

Summary: Routines and Constants common for XML::LibXML and XML::GDOME
Name: perl-XML-LibXML-Common
Version: 0.13
Release: 2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML-Common/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/P/PH/PHISH/XML-LibXML-Common-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl

%description
Routines and Constants common for XML::LibXML and XML::GDOME.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.13-2
- This is not a noarch package. (Ivo Clarysse)

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.13-1
- Fixed site -> vendor. (Matthew Mastracci)

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.13-0
- Updated to release 0.13.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR) 
