# $Id$
# Authority: shuff
# Upstream: Michael Bretterklieber <michael$bretterklieber,com>

%define pear_dir %(pear config-get php_dir 2>/dev/null || echo %{_datadir}/pear)
%define real_name Crypt_CHAP

Summary: PEAR package to generate CHAP packets
Name: php-pear-crypt-chap
Version: 1.5.0
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pear.php.net/package/Crypt_CHAP/

Source0: http://download.pear.php.net/package/Crypt_CHAP-1.5.0.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: php-devel >= 5.1.2
BuildRequires: php-hash
BuildRequires: php-mcrypt
BuildRequires: php-pear >= 1.4.1
Requires: php >= 5.1.2
Requires: php-hash
Requires: php-mcrypt
Requires: php-pear >= 1.4.1

Obsoletes: php-pear-Crypt-CHAP <= %{version}
Provides: php-pear-Crypt-CHAP = %{version}-%{release}

%description
CHAP is a part usualy of PPP (Point-to-Point Protocol) software, implemented in
the authentication subsystem. CHAP avoid's sending plaintext passwords over an
insecure link. The traditional CHAP-MD5 needs the plaintext password stored on
the server. MS-CHAP doesen't need this, but also needs the password either as
NT-Hash and/or as LAN-Manager-Hash. LAN-Manager-Hashes are weak and shouldn't
be used anymore. 

%prep

%build

%install
%{__rm} -rf %{buildroot}
pear install -R %{buildroot} -n %{SOURCE0}
# Remove these hidden files, we don't want to include those
%{__rm} -rf %{buildroot}%{pear_dir}/{.channels,.depdb*,.filemap,.lock,.registry}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%{pear_dir}/*

%changelog
* Wed Sep 29 2010 Steve Huff <shuff@vecna.org> - 1.5.0-1
- Initial package.
