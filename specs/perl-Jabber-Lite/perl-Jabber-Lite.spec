# $Id$
# Authority: dag
# Upstream: Bruce Campbell <beecee$cpan,zerlargal,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jabber-Lite

Summary: Perl standalone library for communicating with Jabber servers
Name: perl-Jabber-Lite
Version: 0.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jabber-Lite/

Source: http://www.cpan.org/modules/by-module/Jabber/Jabber-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Jabber-Lite is a Perl standalone library for communicating
with Jabber servers.

This package contains the following Perl module:

    Jabber::Lite

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Jabber::Lite.3pm*
%dir %{perl_vendorlib}/Jabber/
#%{perl_vendorlib}/Jabber/Lite/
%{perl_vendorlib}/Jabber/Lite.pm

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Initial package. (using DAR)
