# $Id$
# Authority: dag

### EL6 ships with python-mutagen-1.16-2.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name mutagen

Summary: Python module to handle audio metadata
Name: python-mutagen
Version: 1.9
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.sacredchao.net/quodlibet/wiki/Development/Mutagen

Source: http://www.sacredchao.net/~piman/software/mutagen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.0

Provides: mutagen
Obsoletes: mutagen <= %{version}-%{release}

%description
Mutagen is a Python module to handle audio metadata. It supports FLAC, M4A,
MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True Audio, and WavPack
audio files. All versions of ID3v2 are supported, and all standard ID3v2.4
frames are parsed. It can read Xing headers to accurately calculate the
bitrate and length of MP3s. ID3 and APEv2 tags can be edited regardless of
audio format. It can also manipulate Ogg streams on an individual packet/page
level.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc API-NOTES COPYING NEWS README TODO TUTORIAL
%doc %{_mandir}/man1/mid3iconv.1*
%doc %{_mandir}/man1/mid3v2.1*
%doc %{_mandir}/man1/moggsplit.1*
%doc %{_mandir}/man1/mutagen-inspect.1*
%doc %{_mandir}/man1/mutagen-pony.1*
%{_bindir}/mid3iconv
%{_bindir}/mid3v2
%{_bindir}/moggsplit
%{_bindir}/mutagen-inspect
%{_bindir}/mutagen-pony
%{python_sitelib}/mutagen/
%ghost %{python_sitelib}/mutagen/*.pyo

%changelog
* Tue Jan 30 2007 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Thu Aug 17 2006 Dag Wieers <dag@wieers.com> - 1.6-1
- Initial package. (using DAR)
