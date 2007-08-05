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
BuildRequires: perl, perl(Scalar::Util) >= 1.13, perl(File::Remove)
BuildRequires: perl(IO:Scalar) >= 2.110, perl(Object::Realize::Later)
BuildRequires: perl(File::Spec) >= 0.7, perl(Test::Pod >= 1)
BuildRequires: perl(Time::Zone), perl(User::Identity), perl(Digest::HMAC_MD5)
BuildRequires: perl(Mail::Address), perl(Errno), perl(Test::Harness) >= 2.62
BuildRequires: perl(URI) >= 1.23, perl(MIME::Types), perl(Date::Parse)
BuildRequires: perl(Test::More) >= 0.47, perl(MIME::Base64), perl(Sys::Hostname)

%description
E-mail handling.

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
%doc ChangeLog INSTALL LICENSE MANIFEST META.yml README README.FAQ README.todo TODO.v2 examples/
%doc %{_mandir}/man3/Mail::Box.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Mail/
#%{perl_vendorlib}/Mail/Box/
%{perl_vendorlib}/Mail/Box.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 2.073-1
- Initial package. (using DAR)
