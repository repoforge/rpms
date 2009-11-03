# $Id$
# Authority: dag
# Upstream: Ask Bjørn Hansen <ask$perl,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-AlarmCall

Summary: Perl module to handle the logic in timing out calls with alarm()
Name: perl-Sys-AlarmCall
Version: 1.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-AlarmCall/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-AlarmCall-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Sys-AlarmCall is a Perl module to handle the logic in timing out calls
with alarm() and an ALRM handler, allowing nested calls as well.

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
%doc Changes MANIFEST TODO
%doc %{_mandir}/man3/Sys::AlarmCall.3pm*
%dir %{perl_vendorlib}/Sys/
%{perl_vendorlib}/Sys/AlarmCall.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
