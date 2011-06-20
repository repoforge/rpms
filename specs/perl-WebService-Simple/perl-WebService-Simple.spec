# $Id$
# Authority: shuff
# Upstream: Yusuke Wada <yusuke$kamawada,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Simple

Summary: Simple interface to web service APIs
Name: perl-WebService-Simple
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Simple/

Source: http://search.cpan.org/CPAN/authors/id/Y/YU/YUSUKEBE/WebService-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::ConfigHash)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON) >= 2.0
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(URI) >= 1.36
BuildRequires: perl(XML::Feed)
BuildRequires: perl(XML::LibXML)
BuildRequires: perl(XML::Parser::Lite::Tree)
BuildRequires: perl(XML::Parser::Lite::Tree::XPath)
BuildRequires: perl(XML::Simple)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Class::Accessor::Fast)
Requires: perl(Class::Data::ConfigHash)
Requires: perl(Class::Inspector)
Requires: perl(Data::Dumper)
Requires: perl(Digest::MD5)
Requires: perl(JSON) >= 2.0
Requires: perl(LWP::UserAgent)
Requires: perl(UNIVERSAL::require)
Requires: perl(URI) >= 1.36
Requires: perl(XML::Feed)
Requires: perl(XML::LibXML)
Requires: perl(XML::Parser::Lite::Tree)
Requires: perl(XML::Parser::Lite::Tree::XPath)
Requires: perl(XML::Simple)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
WebService::Simple is a simple class to interact with web services.

It's basically an LWP::UserAgent that remembers recurring api URLs and
parameters, plus sugar to parse the results.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

# the example scripts have no shebang line
PERLSCRIPT=$(cat <<'PERL'
opendir( my $EXAMPLE, 'example' );
while( my $script = readdir( $EXAMPLE ) ) {
    next if $script =~ /^\.{1,2}$/;
    open( my $SCRIPT, '<', "example/$script" );
    while ( <$SCRIPT> ) {
        push( @lines, $_ );
    }
    close( $SCRIPT );
    unshift( @lines, "#!%{__perl}\n" );
    open( my $SCRIPT, '>', "example/$script" );
    while ( @lines ) {
        my $line = shift( @lines );
        print $SCRIPT "$line";
    }
    close( $SCRIPT );
}
closedir( $EXAMPLE );
PERL
)
%{__perl} -e "$PERLSCRIPT"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README example/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/WebService/Simple.pm
%{perl_vendorlib}/WebService/Simple/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Mon Jun 20 2011 Steve Huff <shuff@vecna.org> - 0.18-1
- Initial package.
