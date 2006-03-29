# $Id$
# Authority: dries
# Upstream: Olivier Poitrey <rs-pause$rhapsodyk,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Admin-Config

Summary: Read/write Apache like configuration files
Name: perl-Apache-Admin-Config
Version: 0.92
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Admin-Config/

Source: http://search.cpan.org/CPAN/authors/id/R/RS/RSOLIV/Apache-Admin-Config-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
"Apache::Admin::Config" provides an object oriented interface for
reading and writing Apache-like configuration files without affecting
comments, indentation, or truncated lines.

You can easily extract informations from the apache configuration, or
manage htaccess files.
	
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/Admin/Config.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.92-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- Initial package.
