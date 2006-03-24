# $Id$

# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define real_name ExtUtils-ParseXS
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Converts Perl XS code into C code
Name: perl-ExtUtils-ParseXS
Version: 2.15
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-ParseXS/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-ParseXS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module, you can Convert Perl XS code into C code.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/ExtUtils/ParseXS.pm
%{perl_vendorlib}/ExtUtils/xsubpp

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.15-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Initial package.
