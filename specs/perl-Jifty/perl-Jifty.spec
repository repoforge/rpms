# $Id$
# Authority: dag
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jifty

Summary: Perl package that implements an application framework
Name: perl-Jifty
Version: 0.90701
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty/

Source: http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/Jifty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

# remove some bogus autoreq
%filter_from_requires /^perl(Jifty::Plugin::Authentication::Password::Record)/d
%filter_from_requires /^perl(Jifty::Plugin::User::Record)/d
%filter_from_requires /^perl(Jifty::Plugin::OpenID.*/d
%filter_from_requires /^perl(XML.*ExternEnt.*/d

%filter_setup


BuildArch: noarch
BuildRequires: perl >= 2:5.8.3
BuildRequires: perl(Apache2::Const)
BuildRequires: perl(App::CLI) >= 0.08
BuildRequires: perl(Cache::Cache)
BuildRequires: perl(Calendar::Simple)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::Container)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::Trigger) >= 0.13
BuildRequires: perl(Clone) >= 0.27
BuildRequires: perl(CGI) >= 3.30
BuildRequires: perl(CGI::Cookie::Splitter)
BuildRequires: perl(Crypt::CBC)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(CSS::Squish) >= 0.07
BuildRequires: perl(DBD::SQLite) >= 1.11
BuildRequires: perl(Data::Dump::Streamer)
BuildRequires: perl(Data::Page)
BuildRequires: perl(Data::UUID)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Locale)
BuildRequires: perl(Date::Manip)
BuildRequires: perl(Email::Folder)
BuildRequires: perl(Email::LocalDelivery) >= 0.217
BuildRequires: perl(Email::Abstract)
BuildRequires: perl(Email::MIME) >= 1.861
BuildRequires: perl(Email::MIME::Creator) >= 1.450
BuildRequires: perl(Email::MIME::ContentType) >= 1.012
BuildRequires: perl(Email::MIME::CreateHTML)
BuildRequires: perl(Email::MIME::Modifier) >= 1.443
BuildRequires: perl(Email::Send) >= 2.10
BuildRequires: perl(Email::Simple) >= 2.003
BuildRequires: perl(Email::Simple::Creator) >= 1.400
BuildRequires: perl(Exception::Class)
BuildRequires: perl(Exporter::Lite)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::MMagic)
BuildRequires: perl(File::ShareDir) >= 1.00
# RHEL5 has File::Spec 3.12
# however, the changes between 3.12 and 3.14 appear to apply almost entirely
# to Cygwin
#BuildRequires: perl(File::Spec) >= 3.14
BuildRequires: perl(File::Spec) >= 3.12
BuildRequires: perl(File::Temp) >= 0.15
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTML::Lint)
BuildRequires: perl(HTML::Mason) >= 1.3101
BuildRequires: perl(HTML::Mason::Plugin)
BuildRequires: perl(HTTP::Cookies)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Server::Simple) >= 0.35
BuildRequires: perl(HTTP::Server::Simple::Recorder)
BuildRequires: perl(Hash::Merge)
BuildRequires: perl(Hook::LexWrap)
BuildRequires: perl(IPC::PubSub) >= 0.23
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Jifty::DBI) >= 0.57
BuildRequires: perl(JSON::Syck) >= 0.29
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Locale::Maketext::Extract) >= 0.35
BuildRequires: perl(Locale::Maketext::Lexicon) >= 0.77
BuildRequires: perl(Log::Log4perl) >= 1.11
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Types)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(Module::Install::Admin) >= 0.50
BuildRequires: perl(Module::Pluggable) >= 3.7
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Module::Refresh) >= 0.09
BuildRequires: perl(Module::ScanDeps)
BuildRequires: perl(Net::Server::Fork)
BuildRequires: perl(Net::Server::PreFork)
BuildRequires: perl(Object::Declare) >= 0.13
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Scalar::Defer) >= 0.12
# RHEL5 has ExtUtils::Command-1.09 and mysteriously does not include 
# Shell::Command;  however, Shell::Command is only called in a single test in
# the Jifty source
#BuildRequires: perl(Shell::Command)
BuildRequires: perl(ExtUtils::Command)
BuildRequires: perl(String::BufferStack) >= 1.12
BuildRequires: perl(String::Koremutake)
BuildRequires: perl(SQL::ReservedWords)
BuildRequires: perl(SUPER)
BuildRequires: perl(Template::Declare) >= 0.36
BuildRequires: perl(Test::Base) >= 0.44
BuildRequires: perl(Test::Email)
BuildRequires: perl(Test::HTML::Lint)
BuildRequires: perl(Test::HTTP::Server::Simple) >= 0.10
BuildRequires: perl(Test::Log4perl)
BuildRequires: perl(Test::LongString)
BuildRequires: perl(Test::MockModule) >= 0.05
BuildRequires: perl(Test::MockObject) >= 1.07
BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::WWW::Declare) >= 0.01
BuildRequires: perl(Test::WWW::Mechanize) >= 1.04
BuildRequires: perl(Test::WWW::Selenium)
BuildRequires: perl(WWW::Mechanize) >= 1.51
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(URI) >= 1.31
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::Writer) >= 0.601
BuildRequires: perl(XML::Simple)
BuildRequires: perl(XML::XPath)
BuildRequires: perl(version)
BuildRequires: perl(YAML) >= 0.35
BuildRequires: perl(YAML::Syck) >= 0.71
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 2:5.8.3
Requires: perl(Cache::Simple::TimedExpiry)
Requires: perl(Number::RecordLocator)

%description
perl-Jifty is a Perl package that implements an application framework.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find contrib/ doc/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog MANIFEST MANIFEST.SKIP META.yml README SIGNATURE contrib/ doc/ examples/
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/auto/share/dist/
%{perl_vendorlib}/auto/share/dist/*
%{perl_vendorlib}/Jifty.pm
%{perl_vendorlib}/Jifty/
%{_bindir}/jifty

%changelog
* Mon Oct 05 2009 Steve Huff <shuff@vecna.org> - 0.090701-1
- Updated to release 0.090701.
- Builds and installs on RHEL5!
- Still needs more exhaustive testing.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.80408-1
- Updated to release 0.80408.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.71129-1
- Updated to release 0.71129.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.70824-1
- Initial package. (using DAR)
