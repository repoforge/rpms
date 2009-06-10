# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa@bulknews.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Duration-Parse

Summary: Parse string that represents time duration
Name: perl-Time-Duration-Parse
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Duration-Parse/

Source: http://www.cpan.org/modules/by-module/Time/Time-Duration-Parse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::Duration)

%description
Parse string that represents time duration.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Time::Duration::Parse.3pm*
%dir %{perl_vendorlib}/Time/
%dir %{perl_vendorlib}/Time/Duration/
#%{perl_vendorlib}/Time/Duration/Parse/
%{perl_vendorlib}/Time/Duration/Parse.pm

%changelog
* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 0.06-1
- Updated to version 0.06.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
