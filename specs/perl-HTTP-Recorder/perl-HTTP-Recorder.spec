# $Id$
# Authority: dag
# Upstream: Linda Julien <leira$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTTP-Recorder

Summary: Perl module to record interaction with websites
Name: perl-HTTP-Recorder
Version: 0.05
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTTP-Recorder/

Source: http://www.cpan.org/modules/by-module/HTTP/HTTP-Recorder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
HTTP-Recorder is a Perl module to record interaction with websites.

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/HTTP::Recorder.3pm*
%dir %{perl_vendorlib}/HTTP/
%{perl_vendorlib}/HTTP/Recorder/
%{perl_vendorlib}/HTTP/Recorder.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
