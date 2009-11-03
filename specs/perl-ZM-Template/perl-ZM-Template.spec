# $Id$
# Authority: dag
# Upstream: Maxim Kashliak <maxico$softhome,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ZM-Template

Summary: Perl module to merges runtime data with static HTML or plain text
Name: perl-ZM-Template
Version: 0.7.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ZM-Template/

Source: http://www.cpan.org/authors/id/M/MA/MAXICO/ZM-Template-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-ZM-Template is a Perl module to merges runtime data with static HTML
or plain text.

This package contains the following Perl module:

    ZM::Template

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
%doc %{_mandir}/man3/ZM::Template.3pm*
%dir %{perl_vendorlib}/ZM/
%{perl_vendorlib}/ZM/Template.pm

%changelog
* Mon Jul 20 2009 Christoph Maser <cmr@financial.com> - 0.7.2-1
- Updated to version 0.7.2.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Initial package. (using DAR)
