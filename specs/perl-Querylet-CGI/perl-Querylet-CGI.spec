# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Querylet-CGI

Summary: Perl module to turn a querylet into a web application
Name: perl-Querylet-CGI
Version: 0.142
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Querylet-CGI/

Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Querylet-CGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Querylet-CGI is a Perl module to turn a querylet into a web application.

This package contains the following Perl modules:

    Querylet::CGI
    Querylet::CGI::Auto

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Querylet::CGI.3pm*
%doc %{_mandir}/man3/Querylet::CGI::Auto.3pm*
%dir %{perl_vendorlib}/Querylet/
%{perl_vendorlib}/Querylet/CGI/
%{perl_vendorlib}/Querylet/CGI.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.142-1
- Initial package. (using DAR)
