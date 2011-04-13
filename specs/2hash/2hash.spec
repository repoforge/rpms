# $Id$
# Authority: dag

Summary: Tool to simultaneous do MD5 and SHA1 hashing
Name: 2hash
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://trog.qgl.org/20061027/2hash-simultaneous-md5-and-sha1-hashing/

Source: http://trog.qgl.org/download.php/2hash-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#BuildRequires: glibc-static
BuildRequires: libstdc++-devel

%description
2hash simultaneously performs a md5 and a sha1 checksum on file(s).
If you want two checksums for additionally integrity checking, you previously
had to run md5sum and sha1sum serially causing the integrity checks to
take 100% longer than running a single check alone. 2hash runs both hashes
in parallel, only having to read the file once. It allows you to 
get both hash values with only about an 8% time increase over md5 alone,
and only about a 2% time increase over sha1 alone. It runs about 90%
quicker than using both md5 and sha1 one after the other... 

%prep
%setup -n %{name}-v%{version}

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"

%install
%{__rm} -rf %{buildroot}
%{__make} install bindir="%{buildroot}%{_bindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL README
%{_bindir}/2hash

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
