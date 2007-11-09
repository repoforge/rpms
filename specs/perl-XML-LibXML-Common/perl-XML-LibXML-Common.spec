# $Id$
# Authority: dag

### Already ships with 0.13
# ExcludeDist: fc2 fc3 el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-LibXML-Common

Summary: Routines and Constants common for XML::LibXML and XML::GDOME
Name: perl-XML-LibXML-Common
Version: 0.13
Release: 3.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-LibXML-Common/

Source: http://www.cpan.org/modules/by-module/XML/XML-LibXML-Common-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: libxml2-devel
Requires: perl

%description
Routines and Constants common for XML::LibXML and XML::GDOME.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/XML/
%dir %{perl_vendorarch}/XML/LibXML/
%{perl_vendorarch}/XML/LibXML/Common.pm
%dir %{perl_vendorarch}/auto/XML/
%dir %{perl_vendorarch}/auto/XML/LibXML/
%{perl_vendorarch}/auto/XML/LibXML/Common/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-3.2
- Rebuild for Fedora Core 5.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 0.13-3
- Cosmetic fixes.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.13-2
- This is not a noarch package. (Ivo Clarysse)

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.13-1
- Fixed site -> vendor. (Matthew Mastracci)

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.13-0
- Updated to release 0.13.

* Wed May 28 2003 Dag Wieers <dag@wieers.com> - 0.12-0
- Initial package. (using DAR)
