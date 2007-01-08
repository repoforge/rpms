# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-HTTP

Summary: HTTP user-agent component
Name: perl-POE-Component-Client-HTTP
Version: 0.80
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-HTTP/

Source: http://search.cpan.org//CPAN/authors/id/R/RC/RCAPUTO/POE-Component-Client-HTTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A HTTP user-agent component.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES* README
%doc %{_mandir}/man3/POE::*
%{perl_vendorlib}/POE/Component/Client/HTTP.pm
%{perl_vendorlib}/POE/Component/Client/HTTP/
%{perl_vendorlib}/POE/Filter/

%changelog
* Sat Jan 06 2007 Dries Verachtert <dries@ulyssis.org> - 0.80-1
- Updated to release 0.80.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.78-1
- Initial package.
