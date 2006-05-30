# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#40179;&#9787; <cpan$audreyt,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Syck

Summary: Fast YAML loader and dumper
Name: perl-YAML-Syck
Version: 0.45
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Syck/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/YAML-Syck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This package contains a YAML loader and dumper.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/JSON/
%{perl_vendorarch}/YAML/Dumper/
%{perl_vendorarch}/YAML/Loader/
%{perl_vendorarch}/YAML/Syck.p*
%{perl_vendorarch}/auto/YAML/Syck/

%changelog
* Tue May 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.45-1
- Initial package.
