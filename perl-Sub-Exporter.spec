#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-Sub-Exporter
Version  : 0.991
Release  : 45
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-0.991.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-0.991.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsub-exporter-perl/libsub-exporter-perl_0.987-1.debian.tar.xz
Summary  : 'a sophisticated exporter for custom-built routines'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Exporter-license = %{version}-%{release}
Requires: perl-Sub-Exporter-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Getopt::Long)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Install)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Sub-Exporter,
version 0.991:
a sophisticated exporter for custom-built routines

%package dev
Summary: dev components for the perl-Sub-Exporter package.
Group: Development
Provides: perl-Sub-Exporter-devel = %{version}-%{release}
Requires: perl-Sub-Exporter = %{version}-%{release}

%description dev
dev components for the perl-Sub-Exporter package.


%package license
Summary: license components for the perl-Sub-Exporter package.
Group: Default

%description license
license components for the perl-Sub-Exporter package.


%package perl
Summary: perl components for the perl-Sub-Exporter package.
Group: Default
Requires: perl-Sub-Exporter = %{version}-%{release}

%description perl
perl components for the perl-Sub-Exporter package.


%prep
%setup -q -n Sub-Exporter-0.991
cd %{_builddir}
tar xf %{_sourcedir}/libsub-exporter-perl_0.987-1.debian.tar.xz
cd %{_builddir}/Sub-Exporter-0.991
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sub-Exporter-0.991/deblicense/
pushd ..
cp -a Sub-Exporter-0.991 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter
cp %{_builddir}/Sub-Exporter-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter/d13875bde4c7a864ea6cdbc087f79fb0130757df || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter/8a24d0e62a6e0102122cbc87a2322ea45fe869f5 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Exporter.3
/usr/share/man/man3/Sub::Exporter::Cookbook.3
/usr/share/man/man3/Sub::Exporter::Tutorial.3
/usr/share/man/man3/Sub::Exporter::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sub-Exporter/8a24d0e62a6e0102122cbc87a2322ea45fe869f5
/usr/share/package-licenses/perl-Sub-Exporter/d13875bde4c7a864ea6cdbc087f79fb0130757df

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
