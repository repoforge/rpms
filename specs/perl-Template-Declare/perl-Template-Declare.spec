# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Declare

Summary: Perlish declarative templates
Name: perl-Template-Declare
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Declare/

Source: http://search.cpan.org//CPAN/authors/id/J/JE/JESSE/Template-Declare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perlish declarative templates.

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
%doc README SIGNATURE
%doc %{_mandir}/man3/Template::Declare*
%{perl_vendorlib}/Template/Declare.pm
%{perl_vendorlib}/Template/Declare/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
