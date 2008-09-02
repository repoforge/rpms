# $Id$
# Authority: dag
# Upstream: John Gardiner Myers <jgmyers$proofpoint,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Encode-Detect

Summary: Perl module that implements an Encode::Encoding subclass that detects the encoding of data
Name: perl-Encode-Detect
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Encode-Detect/

Source: http://www.cpan.org/modules/by-module/Encode/Encode-Detect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)
BuildRequires: perl(ExtUtils::CBuilder)

%description
Encode-Detect is a Perl module that implements an Encode::Encoding subclass
that detects the encoding of data.

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
%doc Changes LICENSE MANIFEST META.yml
%doc %{_mandir}/man3/Encode::Detect.3pm*
%doc %{_mandir}/man3/Encode::Detect::*.3pm*
%dir %{perl_vendorarch}/auto/Encode/
%{perl_vendorarch}/auto/Encode/Detect/
%dir %{perl_vendorarch}/Encode/
%{perl_vendorarch}/Encode/Detect/
%{perl_vendorarch}/Encode/Detect.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
