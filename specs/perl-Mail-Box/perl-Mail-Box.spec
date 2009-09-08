# $Id$
# Authority: dag
# Upstream: Mark Overmeer

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Box

Summary: E-mail handling
Name: perl-Mail-Box
Version: 2.091
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Box/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Box-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml requires
BuildRequires: perl(Date::Format)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(Digest::HMAC_MD5)
%{?el5:BuildRequires: perl(Encode) >= 2.26}
BuildRequires: perl(Errno)
BuildRequires: perl(File::Remove) >= 0.20
BuildRequires: perl(File::Spec) >= 0.7
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(MIME::Types) >= 1.004
BuildRequires: perl(Mail::Address)
BuildRequires: perl(Object::Realize::Later) >= 0.14
BuildRequires: perl(Scalar::Util) >= 1.13
BuildRequires: perl(Sys::Hostname)
#BuildRequires: perl(TAP::Harness) >= 3.00
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Time::Zone)
BuildRequires: perl(URI) >= 1.23
BuildRequires: perl(User::Identity) >= 0.90

### Missing provides from autoprov
Provides: perl(Mail::Message::Body::Construct) = %{version}
Provides: perl(Mail::Message::Construct) = %{version}
Provides: perl(Mail::Message::Construct::Bounce) = %{version}
Provides: perl(Mail::Message::Construct::Build) = %{version}
Provides: perl(Mail::Message::Construct::Forward) = %{version}
Provides: perl(Mail::Message::Construct::Read) = %{version}
Provides: perl(Mail::Message::Construct::Rebuild) = %{version}
Provides: perl(Mail::Message::Construct::Reply) = %{version}
Provides: perl(Mail::Message::Construct::Text) = %{version}

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
%doc %{_mandir}/man3/Mail::*.3pm*
%{perl_vendorlib}/Mail/

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 2.091-1
- Updated to version 2.091.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 2.090-1
- Updated to version 2.090.

* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 2.084-1
- Updated to release 2.084.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.082-1
- Updated to release 2.082.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 2.081-1
- Updated to release 2.081.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 2.080-1
- Updated to release 2.080.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 2.079-1
- Updated to release 2.079.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 2.078-1
- Updated to release 2078.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 2.075-1
- Updated to release 2.075.

* Wed Sep 12 2007 Dag Wieers <dag@wieers.com> - 2.073-2
- Added static perl(Mail::Message) provides. (Josh Kelley)

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 2.073-1
- Initial package. (using DAR)
