# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Parser-Syck

Summary: Wrapper for the YAML Parser Extension: libsyck
Name: perl-YAML-Parser-Syck
Version: 0.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Parser-Syck/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-Parser-Syck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, syck-devel

%description
Perl Wrapper for the YAML Parser Extension: libsyck.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -rf %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/YAML/
%dir %{perl_vendorarch}/YAML/Parser/
%{perl_vendorarch}/YAML/Parser/Syck.pm
%dir %{perl_vendorarch}/auto/YAML/
%dir %{perl_vendorarch}/auto/YAML/Parser/
%{perl_vendorarch}/auto/YAML/Parser/Syck/

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
