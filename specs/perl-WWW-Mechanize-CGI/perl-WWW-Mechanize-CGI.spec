# $Id$
# Authority: dag
# Upstream: Marcus Ramberg <mramberg$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Mechanize-CGI

Summary: Use WWW::Mechanize with CGI applications
Name: perl-WWW-Mechanize-CGI
Version: 0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Mechanize-CGI/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-CGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Summary: Use WWW::Mechanize with CGI applications.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/WWW::Mechanize::CGI.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Mechanize/
#%{perl_vendorlib}/WWW/Mechanize/CGI/
%{perl_vendorlib}/WWW/Mechanize/CGI.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
