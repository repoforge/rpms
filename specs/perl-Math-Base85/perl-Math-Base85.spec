# $Id$
# Authority: dries
# Upstream: Tony Monroe <tmonroe+cpan$nog,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Base85

Summary: Base 85 numbers, as referenced by RFC 1924
Name: perl-Math-Base85
Version: 0.2
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Base85/

Source: http://search.cpan.org/CPAN/authors/id/T/TM/TMONROE/Math-Base85-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module handles numbers in base 85, via strings and Math::BigInt.
For more information, read the module or rfc1924.txt.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/Base85.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
