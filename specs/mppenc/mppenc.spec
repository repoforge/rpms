# $Id$
# Authority: dag

Summary: Musepack encoder
Name: mppenc
Version: 1.16
Release: 1
License: LGPL
Group: Applications/Multimedia
URL: http://www.musepack.net/

Source: http://files.musepack.net/source/mppenc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cmake
BuildRequires: nasm

%description
This program handles encoding of the MPC format, which is an audio
compression format with a strong emphasis on high quality. It's not
lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much
smaller MPC file. It is based on the MPEG-1 Layer-2 / MP2 algorithms,
but since 1997 it has rapidly developed and vastly improved and is now
at an advanced stage in which it contains heavily optimized and
patentless code.

%prep
%setup

%build
cmake -DCMAKE_INSTALL_PREFIX:="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog
%{_bindir}/mppenc

%changelog
* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 1.16-1
- Initial package. (using DAR)
