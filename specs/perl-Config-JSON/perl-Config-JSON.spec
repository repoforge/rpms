# $Id$
# Authority: dries
# Upstream: JT Smith <jt%20at%20plainblack%20dot%20com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-JSON

Summary: JSON based config file system
Name: perl-Config-JSON
Version: 1.0.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-JSON/

Source: http://search.cpan.org/CPAN/authors/id/R/RI/RIZEN/Config-JSON-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A JSON based config file system.

%prep
%setup -n %{real_name}

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
%doc %{_mandir}/man3/Config::JSON*
%{perl_vendorlib}/Config/JSON.pm

%changelog
* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1
- Initial package.
