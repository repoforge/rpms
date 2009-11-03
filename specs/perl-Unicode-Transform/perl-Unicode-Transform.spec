# $Id$
# Authority: dag
# Upstream: SADAHIRO Tomoyuki <SADAHIRO$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Transform

Summary: Perl module for conversion among Unicode Transformation Formats
Name: perl-Unicode-Transform
Version: 0.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Transform/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Transform-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Unicode-Transform is a Perl module for conversion among Unicode
Transformation Formats.

This package contains the following Perl module:

    Unicode::Transform

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Unicode::Transform.3pm*
%dir %{perl_vendorarch}/Unicode/
%{perl_vendorarch}/Unicode/Transform.pm
%dir %{perl_vendorarch}/auto/Unicode/
%{perl_vendorarch}/auto/Unicode/Transform/

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.34-1
- Initial package. (using DAR)
