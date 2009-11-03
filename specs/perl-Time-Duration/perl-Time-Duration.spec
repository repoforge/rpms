# $Id$
# Authority: dag
# Upstream: , Sean M. Burke C<sburke@cpan.org>, all rights

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Duration

Summary: Perl module to provide rounded or exact English expression of durations
Name: perl-Time-Duration
Version: 1.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Duration/

Source: http://www.cpan.org/modules/by-module/Time/Time-Duration-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

%description
perl-Time-Duration is a Perl module to provide rounded or exact English
expression of durations.

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
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Time::Duration.3pm*
%dir %{perl_vendorlib}/Time/
%{perl_vendorlib}/Time/Duration.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
