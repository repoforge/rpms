# $Id$
# Authority: dries
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Untaint

Summary: Process CGI input parameters
Name: perl-CGI-Untaint
Version: 1.25
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Untaint/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Untaint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Process CGI input parameters.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Untaint.pm
%{perl_vendorlib}/CGI/Untaint/

%changelog
* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Initial package.
