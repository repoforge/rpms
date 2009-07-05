# $Id$
# Authority: dries
# Upstream: Piers Harding <piers$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Inline-BC

Summary: Inline ILSM for bc the arbitrary precision math Language
Name: perl-Inline-BC
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Inline-BC/

Source: http://www.cpan.org/modules/by-module/Inline/Inline-BC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Inline::BC is an ILSM (Inline Support Language Module ) for Gnu bc, the arbitrary
precision numeric processing language.  Inline::BC - like other ILSMs - allows you
compile (well - render to byte code ), and run Gnu bc code within your Perl
program.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Inline/BC.pm
%dir %{perl_vendorarch}/auto/Inline/
%{perl_vendorarch}/auto/Inline/BC/

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.08-1
- Updated to version 0.08.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
