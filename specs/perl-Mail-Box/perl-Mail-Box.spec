# $Id$
# Authority: dag
# Upstream: Mark Overmeer

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Box

Summary: E-mail handling
Name: perl-Mail-Box
Version: 2.073
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Box/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Box-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Date::Parse)
BuildRequires: perl(Digest::HMAC_MD5)
BuildRequires: perl(Errno)
BuildRequires: perl(File::Remove)
BuildRequires: perl(File::Spec) >= 0.7
BuildRequires: perl(IO::Scalar) >= 2.110
BuildRequires: perl(Mail::Address)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(MIME::Types)
BuildRequires: perl(Object::Realize::Later)
BuildRequires: perl(Scalar::Util) >= 1.13
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::Harness)
#BuildRequires: perl(Test::Harness) >= 2.62
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Pod) >= 1
BuildRequires: perl(Time::Zone)
BuildRequires: perl(User::Identity)
BuildRequires: perl(URI) >= 1.23

%description
E-mail handling.

%prep
%setup -n %{real_name}-%{version}

%build
yes n | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL LICENSE MANIFEST META.yml README README.FAQ README.todo TODO.v2 examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Mail/

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 2.073-1
- Initial package. (using DAR)
