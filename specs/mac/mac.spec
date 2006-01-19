# $Id$
# Authority: matthias

Summary: Monkey's Audio Codec (MAC) utility and library
Name: mac
Version: 3.99
Release: 1.u4b4
License: See License.htm
Group: System Environment/Libraries
URL: http://supermmx.org/linux/mac/
Source: http://dl.sf.net/mac-port/mac-%{version}-u4-b4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, nasm

%description
Monkey’s Audio is a fast and easy way to compress digital music. Unlike
traditional methods such as mp3, ogg, or lqt that permanently discard
quality to save space, Monkey’s Audio only makes perfect, bit-for-bit
copies of your music. That means it always sounds perfect  – exactly the
same as the original. Even though the sound is perfect, it still saves a
lot of space.


%package devel
Summary: Development files for the Monkey's Audio Codec library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Monkey’s Audio is a fast and easy way to compress digital music. Unlike
traditional methods such as mp3, ogg, or lqt that permanently discard
quality to save space, Monkey’s Audio only makes perfect, bit-for-bit
copies of your music. That means it always sounds perfect  – exactly the
same as the original. Even though the sound is perfect, it still saves a
lot of space.

This package contains the development files for theMonkey's Audio Codec
library.


%prep
%setup -n %{name}-%{version}-u4-b4


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc src/Credits.txt src/History.txt src/License.htm src/Readme.htm
%{_bindir}/mac
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mac/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Thu Jan 19 2006 Matthias Saou <http://freshrpms.net/> 3.99-1.u4b4
- Update to 3.99-u4-b4.
- Still only works on x86, so if anyone feels like fixing this...

* Thu May 26 2005 Matthias Saou <http://freshrpms.net/> 3.99-1.u4b3
- Initial RPM release.

