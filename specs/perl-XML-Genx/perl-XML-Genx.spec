# $Id$
# Authority: dries
# Upstream: Dominic Mitchell <cpan$happygiraffe,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Genx

Summary: Small correct XML writer
Name: perl-XML-Genx
Version: 0.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Genx/

Source: http://search.cpan.org//CPAN/authors/id/H/HD/HDM/XML-Genx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(Module::Build)

%description
A small simple correct XML writer.

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
%doc %{_mandir}/man3/XML::Genx*.3pm*
%dir %{perl_vendorarch}/XML/
%{perl_vendorarch}/XML/Genx.pm
%{perl_vendorarch}/XML/Genx/
%dir %{perl_vendorarch}/auto/XML/
%{perl_vendorarch}/auto/XML/Genx/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
