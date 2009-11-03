# $Id$
# Authority: dag
# Upstream: Maxim Kashliak <maxico$softhome,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ZM-Session

Summary: Perl module that implements a sessions manager for CGI
Name: perl-ZM-Session
Version: 0.2.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ZM-Session/

Source: http://www.cpan.org/authors/id/M/MA/MAXICO/ZM-Session-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-ZM-Session is a Perl module that implements a sessions manager for CGI.

This package contains the following Perl module:

    ZM::Session

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
%doc MANIFEST README
%doc %{_mandir}/man3/ZM::Session.3pm*
%dir %{perl_vendorlib}/ZM/
%{perl_vendorlib}/ZM/Session.pm

%changelog
* Mon Jul 20 2009 Christoph Maser <cmr@financial.com> - 0.2.1-1
- Updated to version 0.2.1.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Initial package. (using DAR)
