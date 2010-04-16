# $Id$
# Upstream: David Romano <unobe@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name WWW-Facebook-API

Summary: Facebook API implementation
Name: perl-WWW-Facebook-API
Version: 0.4.18
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Facebook-API

Source: http://search.cpan.org/CPAN/authors/id/U/UN/UNOBE/WWW-Facebook-API-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON::Any)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Readonly)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(version)
Requires: perl(Crypt::SSLeay)
Requires: perl(Digest::MD5)
Requires: perl(JSON::Any)
Requires: perl(LWP::UserAgent)
Requires: perl(Readonly)
Requires: perl(Time::HiRes)
Requires: perl(version)

%filter_from_requires /^perl*/d
%filter_setup


%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

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
%doc %{_mandir}/man3/WWW::Facebook::API.3pm*
%doc %{_mandir}/man3/WWW::Facebook::API::Admin.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Application.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Auth.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Canvas.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Comments.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Connect.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Data.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Events.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Exception.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::FBML.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::FQL.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Feed.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Friends.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Groups.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Intl.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Links.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::LiveMessage.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Message.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Notes.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Notifications.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Pages.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Permissions.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Photos.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Profile.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::SMS.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Status.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Stream.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Users.3pm.gz
%doc %{_mandir}/man3/WWW::Facebook::API::Video.3pm.gz
%dir %{perl_vendorlib}/
%{perl_vendorlib}/WWW/Facebook/API.pm
%{perl_vendorlib}/WWW/Facebook/API/Admin.pm
%{perl_vendorlib}/WWW/Facebook/API/Application.pm
%{perl_vendorlib}/WWW/Facebook/API/Auth.pm
%{perl_vendorlib}/WWW/Facebook/API/Canvas.pm
%{perl_vendorlib}/WWW/Facebook/API/Comments.pm
%{perl_vendorlib}/WWW/Facebook/API/Connect.pm
%{perl_vendorlib}/WWW/Facebook/API/Data.pm
%{perl_vendorlib}/WWW/Facebook/API/Events.pm
%{perl_vendorlib}/WWW/Facebook/API/Exception.pm
%{perl_vendorlib}/WWW/Facebook/API/FBML.pm
%{perl_vendorlib}/WWW/Facebook/API/FQL.pm
%{perl_vendorlib}/WWW/Facebook/API/Feed.pm
%{perl_vendorlib}/WWW/Facebook/API/Friends.pm
%{perl_vendorlib}/WWW/Facebook/API/Groups.pm
%{perl_vendorlib}/WWW/Facebook/API/Intl.pm
%{perl_vendorlib}/WWW/Facebook/API/Links.pm
%{perl_vendorlib}/WWW/Facebook/API/LiveMessage.pm
%{perl_vendorlib}/WWW/Facebook/API/Message.pm
%{perl_vendorlib}/WWW/Facebook/API/Notes.pm
%{perl_vendorlib}/WWW/Facebook/API/Notifications.pm
%{perl_vendorlib}/WWW/Facebook/API/Pages.pm
%{perl_vendorlib}/WWW/Facebook/API/Permissions.pm
%{perl_vendorlib}/WWW/Facebook/API/Photos.pm
%{perl_vendorlib}/WWW/Facebook/API/Profile.pm
%{perl_vendorlib}/WWW/Facebook/API/SMS.pm
%{perl_vendorlib}/WWW/Facebook/API/Status.pm
%{perl_vendorlib}/WWW/Facebook/API/Stream.pm
%{perl_vendorlib}/WWW/Facebook/API/Users.pm
%{perl_vendorlib}/WWW/Facebook/API/Video.pm


%changelog
* Fri Apr 16 2010 Christoph Maser <cmr.financial.com> - 0.4.18-1
- initial package
