# $Id$
# Authority: dries
# Upstream: Eric J. Roode <sdn,crams20944$zoemail,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Readonly-XS

Summary: Companion module to Readonly.pm
Name: perl-Readonly-XS
Version: 1.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Readonly-XS/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROODE/Readonly-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is a companion module to Readonly.pm.  You do not use
Readonly::XS directly.  Instead, once it is installed, Readonly.pm
will detect this and will use it for creating read-only scalars.  This
results in a significant speed improvement.  This does not speed up
read-only arrays or hashes.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Readonly/
%{perl_vendorarch}/Readonly/XS.pm
%dir %{perl_vendorarch}/auto/Readonly/
%{perl_vendorarch}/auto/Readonly/XS/

%changelog
* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
