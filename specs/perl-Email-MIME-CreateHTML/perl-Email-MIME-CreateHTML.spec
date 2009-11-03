# $Id$
# Authority: dag
# Upstream: BBC (British Broadcasting Corporation) <cpan$bbc,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-MIME-CreateHTML

Summary: Multipart HTML Email builder
Name: perl-Email-MIME-CreateHTML
Version: 1.026
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-MIME-CreateHTML/

Source: http://www.cpan.org/modules/by-module/Email/Email-MIME-CreateHTML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Multipart HTML Email builder.

This package contains the following Perl module:

    Email::MIME::CreateHTML

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
%doc COPYING Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Email::MIME::CreateHTML.3pm*
%doc %{_mandir}/man3/Email::MIME::CreateHTML::Resolver.3pm*
%doc %{_mandir}/man3/Email::MIME::CreateHTML::Resolver::Cached.3pm*
%doc %{_mandir}/man3/Email::MIME::CreateHTML::Resolver::Filesystem.3pm*
%doc %{_mandir}/man3/Email::MIME::CreateHTML::Resolver::LWP.3pm*
%dir %{perl_vendorlib}/Email/
%dir %{perl_vendorlib}/Email/MIME/
%{perl_vendorlib}/Email/MIME/CreateHTML/
%{perl_vendorlib}/Email/MIME/CreateHTML.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.026-1
- Initial package. (using DAR)
