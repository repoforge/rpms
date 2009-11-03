# $Id$
# Authority: dag
# Upstream: Randal L. Schwartz <merlyn$stonehenge,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Prototype

Summary: Perl module to create a CGI application by subclassing
Name: perl-CGI-Prototype
Version: 0.9053
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Prototype/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Prototype-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-CGI-Prototype is a Perl module to create a CGI application by subclassing.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/CGI::Prototype.3pm*
%doc %{_mandir}/man3/CGI::Prototype::Hidden.3pm*
%dir %{perl_vendorlib}/CGI/
%{perl_vendorlib}/CGI/Prototype/
%{perl_vendorlib}/CGI/Prototype.pm

%changelog
* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.9053-1
- Initial package. (using DAR)
