# $Id$
# Authority: dag
# Upstream: Jesse Vincent <jesse+cpan$fsck,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jifty

Summary: Perl package that implements an application framework
Name: perl-Jifty
Version: 0.80408
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty/

Source: http://www.cpan.org/modules/by-module/Jifty/Jifty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.3
BuildRequires: perl(App::CLI) >= 0.03
BuildRequires: perl(Cache::Cache)
BuildRequires: perl(Calendar::Simple)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::Container)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::Trigger) >= 0.12
BuildRequires: perl(Clone) >= 0.27
BuildRequires: perl(CGI) >= 3.19
BuildRequires: perl(CGI::Cookie::Splitter)
BuildRequires: perl(Crypt::CBC)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(CSS::Squish) >= 0.07
BuildRequires: perl(DBD::SQLite) >= 1.11
BuildRequires: perl(Data::Page)
BuildRequires: perl(Data::UUID)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Locale)
BuildRequires: perl(Date::Manip)
BuildRequires: perl(Email::Folder)
BuildRequires: perl(Email::LocalDelivery) >= 0.217
BuildRequires: perl(Email::MIME)
BuildRequires: perl(Email::MIME::Creator)
BuildRequires: perl(Email::MIME::ContentType)
BuildRequires: perl(Email::MIME::CreateHTML)
BuildRequires: perl(Email::MIME::Modifier)
BuildRequires: perl(Email::Send) >= 1.99
BuildRequires: perl(Email::Simple)
BuildRequires: perl(Email::Simple::Creator)
BuildRequires: perl(Exporter::Lite)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.11
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::MMagic)
BuildRequires: perl(File::ShareDir) >= 0.04
BuildRequires: perl(File::Spec) >= 3.14
BuildRequires: perl(File::Temp) >= 0.15
BuildRequires: perl(HTML::Entities)
BuildRequires: perl(HTML::Lint)
BuildRequires: perl(HTML::Mason) >= 1.3101
BuildRequires: perl(HTML::Mason::Plugin)
BuildRequires: perl(HTTP::Cookies)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Server::Simple) >= 0.26
BuildRequires: perl(HTTP::Server::Simple::Recorder)
BuildRequires: perl(Hash::Merge)
BuildRequires: perl(Hook::LexWrap)
BuildRequires: perl(IPC::PubSub) >= 0.23
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Jifty::DBI) >= 0.47
BuildRequires: perl(JSON::Syck) >= 0.15
BuildRequires: perl(Locale::Maketext::Extract) >= 0.20
BuildRequires: perl(Locale::Maketext::Lexicon) >= 0.60
BuildRequires: perl(Log::Log4perl) >= 1.04
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Types)
BuildRequires: perl(Module::Pluggable) >= 3.5
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(Module::Refresh)
BuildRequires: perl(Module::ScanDeps)
BuildRequires: perl(Object::Declare) >= 0.13
BuildRequires: perl(PadWalker)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Scalar::Defer) >= 0.10
BuildRequires: perl(Shell::Command)
BuildRequires: perl(String::Koremutake)
BuildRequires: perl(SQL::ReservedWords)
BuildRequires: perl(Template::Declare) >= 0.26
BuildRequires: perl(Test::Base)
BuildRequires: perl(Test::Log4perl)
BuildRequires: perl(Test::LongString)
BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::WWW::Mechanize) >= 1.04
BuildRequires: perl(Test::WWW::Selenium)
BuildRequires: perl(WWW::Mechanize) >= 1.04
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(URI) >= 1.31
BuildRequires: perl(XML::Writer) >= 0.601
BuildRequires: perl(XML::Simple)
BuildRequires: perl(XML::XPath)
BuildRequires: perl(version)
BuildRequires: perl(YAML) >= 0.35
BuildRequires: perl(YAML::Syck) >= 0.71
Requires: perl >= 2:5.8.3

%description
perl-Jifty is a Perl package that implements an application framework.

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

### Clean up docs
find contrib/ doc/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog MANIFEST MANIFEST.SKIP META.yml README SIGNATURE contrib/ doc/ examples/
%doc %{_mandir}/man3/Jifty.3pm*
#%{perl_vendorlib}/Jifty/
%{perl_vendorlib}/Jifty.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.80408-1
- Updated to release 0.80408.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.71129-1
- Updated to release 0.71129.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.70824-1
- Initial package. (using DAR)
